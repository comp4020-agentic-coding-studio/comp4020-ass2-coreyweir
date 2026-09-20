import { existsSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

// The published spec for this deliverable, as tests. These assert the contract
// the course makes — what must be true of the site — not how it is built, so
// they survive a change of approach to the content.

interface ApiNode {
  id: string;
  type: string;
  meta?: Record<string, unknown>;
}

interface CourseApi {
  course: { code: string };
  nodes: ApiNode[];
}

const api = JSON.parse(readFileSync(resolve("dist/api/index.json"), "utf8")) as CourseApi;
const ofType = (type: string): ApiNode[] => api.nodes.filter((node) => node.type === type);

const TEACHING_WEEKS = Array.from({ length: 12 }, (_, i) => i + 1);

describe("the course this site promises", () => {
  it("keeps the three course-code digits this repo was allocated", () => {
    expect(api.course.code).toMatch(/^SLOP\d815$/);
  });

  it("teaches in every one of its twelve weeks", () => {
    const taught = [...ofType("sessions"), ...ofType("lectures")];
    const weeks = new Set(taught.map((node) => Number(node.meta?.week)));
    const missing = TEACHING_WEEKS.filter((week) => !weeks.has(week));
    expect(missing, `no teaching material in week ${missing.join(", ")}`).toEqual([]);
  });

  it("assesses exactly 100% of the course", () => {
    const weights = ofType("assessments").map((node) => Number(node.meta?.weight));
    const total = weights.reduce((sum, weight) => sum + weight, 0);
    expect(total, `assessment weights are ${weights.join(" + ")}`).toBe(100);
  });

  it("carries at least one lecture whose deck was really built", () => {
    const declared = ofType("lectures").filter((node) => typeof node.meta?.slides === "string");
    expect(declared.length, "no lecture declares a `slides:` deck").toBeGreaterThan(0);

    const dangling = declared.filter((node) => {
      const route = String(node.meta?.slides).replace(/^\/+|\/+$/g, "");
      return !existsSync(resolve("dist", route, "index.html"));
    });
    expect(dangling.map((node) => node.id), "lecture links to a deck that was not built").toEqual(
      [],
    );
  });
});
