class FoamCushionModel extends HTMLElement {
  constructor() {
    super();
    this.root = this.attachShadow({ mode: "closed" });
    this._rotating = true;
    this.illo = null;
    this.canvas = null;
  }

  setRotating(value) {
    this._rotating = value;
  }

  getRotating() {
    return this._rotating;
  }

  connectedCallback() {
    this.render();
  }

  startDrag() {
    this.setRotating(false);
    this.canvas.style.cursor = "grabbing";
  }

  endDrag() {
    this.setRotating(true);
    this.canvas.style.cursor = "grab";
  }

  render() {
    this.canvas = document.createElement("canvas");
    let canvas = this.canvas;
    canvas.width = 200;
    canvas.height = 200;
    canvas.style.backgroundColor = "black";
    canvas.style.display = "block";
    canvas.style.margin = "auto";
    canvas.style.cursor = "grab";
    this.root.appendChild(canvas);

    let maxCushionArcHeight = 20;

    this.illo = new Zdog.Illustration({
      element: canvas,
      zoom: 0.2,
      dragRotate: true,
      onDragStart: () => this.startDrag(),
      onDragEnd: () => this.endDrag(),
      rotate: { y: -Zdog.TAU / 16, x: -Zdog.TAU / 32 },
    });

    let anchor = new Zdog.Anchor({
      addTo: this.illo,
      translate: { y: 100 },
      rotate: { x: Zdog.TAU / 4, y: Zdog.TAU / 2 },
    });

    let squareFront = new Zdog.Rect({
      addTo: anchor,
      width: 540,
      height: 380,
      stroke: 10,
      color: "#D5CACE",
      fill: true,
    });
    let roundTop = new Zdog.Shape({
      addTo: anchor,
      path: [
        { x: -540 / 2, y: -380 / 2 },
        {
          bezier: [
            { x: -540 / 2, y: -500 },
            { x: 540 / 2, y: -500 },
            { x: 540 / 2, y: -380 / 2 },
          ],
        },
      ],
      stroke: 10,
      color: "#D5CACE",
      fill: true,
    });
    squareFront.copy({
      translate: { z: -74 },
    });
    roundTop.copy({
      translate: { z: -74 },
    });

    let roundLine = new Zdog.Shape({
      addTo: anchor,
      path: [
        { x: -540 / 2, y: -380 / 2 },
        {
          bezier: [
            { x: -540 / 2, y: -500 },
            { x: 540 / 2, y: -500 },
            { x: 540 / 2, y: -380 / 2 },
          ],
        },
        { x: 540 / 2, y: -380 / 2, z: -74 },
        {
          bezier: [
            { x: 540 / 2, y: -500, z: -74 },
            { x: -540 / 2, y: -500, z: -74 },
            { x: -540 / 2, y: -380 / 2, z: -74 },
          ],
        },
        { x: -540 / 2, y: -380 / 2 },
      ],
      closed: true,
      stroke: 10,
      color: "#D5CACE",
      fill: true,
    });

    let left = new Zdog.Shape({
      addTo: anchor,
      path: [
        { x: -540 / 2, y: -380 / 2, z: 0 },
        { x: -540 / 2, y: -380 / 2, z: -74 },
        { x: -540 / 2, y: 380 / 2, z: -74 },
        { x: -540 / 2, y: 380 / 2, z: 0 },
      ],
      closed: true,
      stroke: 10,
      color: "#D5CACE",
      fill: true,
    });
    left.copy({
      translate: { x: 540 },
    });

    let bottom = new Zdog.Shape({
      addTo: anchor,
      path: [
        { x: -540 / 2, y: 380 / 2, z: 0 },
        { x: -540 / 2, y: 380 / 2, z: -74 },
        { x: 540 / 2, y: 380 / 2, z: -74 },
        { x: 540 / 2, y: 380 / 2, z: 0 },
      ],
      closed: true,
      stroke: 10,
      color: "#D5CACE",
      fill: true,
    });

    this.illo.updateRenderGraph();
    this.animate();
  }

  animate() {
    if (this.getRotating()) {
      this.illo.rotate.y += 0.01;
    }
    this.illo.updateRenderGraph();
    requestAnimationFrame(() => this.animate());
  }
}

customElements.define("foam-cushion-model", FoamCushionModel);
