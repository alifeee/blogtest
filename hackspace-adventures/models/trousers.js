class TrousersModel extends HTMLElement {
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
    let canvas = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    canvas.setAttribute("width", "200");
    canvas.setAttribute("height", "200");
    canvas.style.width = "100%";
    canvas.style.height = "100%";
    canvas.style.cursor = "grab";
    this.root.appendChild(canvas);
    this.canvas = canvas;

    let maxCushionArcHeight = 20;

    this.illo = new Zdog.Illustration({
      element: canvas,
      zoom: 0.25,
      dragRotate: true,
      onDragStart: () => this.startDrag(),
      onDragEnd: () => this.endDrag(),
      rotate: { y: -Zdog.TAU / 16, x: Zdog.TAU / 32 },
    });

    let anchor = new Zdog.Anchor({
      addTo: this.illo,
      translate: { y: -500 },
    });

    let leftLeg = new Zdog.Cylinder({
      addTo: anchor,
      diameter: 200,
      length: 1050,
      stroke: false,
      color: "#A7A29E",
      backface: "black",
      rotate: { x: Zdog.TAU / 4 },
      translate: { x: -160 },
    });

    let stitch = new Zdog.Ellipse({
      addTo: leftLeg,
      diameter: 205,
      stroke: 10,
      color: "#633926",
      translate: { z: -500 },
    });

    let rightLeg = leftLeg.copy({
      translate: { x: 160 },
    });

    new Zdog.Ellipse({
      addTo: rightLeg,
      diameter: 205,
      stroke: 10,
      color: "#633926",
      translate: { z: -500 },
    });

    let top = new Zdog.Box({
      addTo: anchor,
      width: 460,
      height: 200,
      depth: 200,
      stroke: false,
      color: "#A7A29E",
      translate: { y: -460 },
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

customElements.define("trousers-model", TrousersModel);
