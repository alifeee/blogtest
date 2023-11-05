class BookendModel extends HTMLElement {
  constructor() {
    super();
    this.root = this.attachShadow({ mode: "closed" });
    this._rotating = true;
    this.illo = null;
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

  render() {
    let canvas = document.createElement("canvas");
    canvas.width = 200;
    canvas.height = 200;
    canvas.style.backgroundColor = "black";
    canvas.style.display = "block";
    canvas.style.margin = "auto";
    this.root.appendChild(canvas);

    this.illo = new Zdog.Illustration({
      element: canvas,
      zoom: 4,
      dragRotate: true,
      onDragStart: () => this.setRotating(false),
      onDragEnd: () => this.setRotating(true),
    });

    new Zdog.Ellipse({
      addTo: this.illo,
      diameter: 20,
      translate: { z: 10 },
      stroke: 5,
      color: "#636",
    });

    new Zdog.Rect({
      addTo: this.illo,
      width: 20,
      height: 20,
      translate: { z: -10 },
      stroke: 3,
      color: "#E62",
      fill: true,
    });

    // start animation
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

customElements.define("bookend-model", BookendModel);
