import Node from "../Node";

describe("Node", () => {
  test("constructor()", () => {
    const n = new Node(100);
    expect(n).toBeTruthy();
    expect(n.data).toBe(100);
    expect(n.next).toBe(null);
    expect(n.prev).toBe(null);
  });

  test("data", () => {
    const n1 = new Node(100);
    expect(n1.data).toBe(100);
    const n2 = new Node("foo bar");
    expect(n2.data).toBe("foo bar");
  });

  test("next", () => {
    const n1 = new Node(100);
    const n2 = new Node(200);
    n1.next = n2;
    expect(n1.next.data).toBe(n2.data);
  });

  test("prev", () => {
    const n1 = new Node(100);
    const n2 = new Node(200);
    n2.prev = n1;
    expect(n2.prev.data).toBe(n1.data);
  });
});
