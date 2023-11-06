function interpolate(a, b, percent) {
  // sqrt to make it non-linear
  if (percent <= 0) {
    return a;
  }
  return a + (b - a) * Math.sqrt(Math.sqrt(percent));
}

function colorCycle(index) {
  let colors = ["#D84D60", "#D84D60", "#79B9D4", "#DCD18F", "#79B9D4"];
  return colors[index % colors.length];
}

class CushionModel extends HTMLElement {
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

    let maxCushionArcHeight = 20;

    this.illo = new Zdog.Illustration({
      element: canvas,
      zoom: 3,
      dragRotate: true,
      onDragStart: () => this.setRotating(false),
      onDragEnd: () => this.setRotating(true),
      rotate: { y: -Zdog.TAU / 4, x: -Zdog.TAU / 32 },
    });

    for (let direction = -1; direction <= 1; direction += 2) {
      for (let y = 1; y < 30; y += 1) {
        let percent;
        if (y < 15) {
          percent = y / 15;
        } else {
          percent = (30 - y) / 15;
        }
        let z = direction * interpolate(0, maxCushionArcHeight, percent);
        new Zdog.Shape({
          addTo: this.illo,
          translate: { x: -15, y: -15 },
          path: [
            { x: 0, y: y },
            {
              arc: [
                {
                  x: 15,
                  y: y,
                  z: z,
                },
                { x: 30, y: y, z: 0 },
              ],
            },
          ],
          closed: false,
          color: colorCycle(y),
        });
      }
    }

    for (let direction = -1; direction <= 1; direction += 2) {
      for (let x = 1; x < 30; x += 1) {
        let percent;
        if (x < 15) {
          percent = x / 15;
        } else {
          percent = (30 - x) / 15;
        }
        let z = direction * interpolate(0, maxCushionArcHeight, percent);
        new Zdog.Shape({
          addTo: this.illo,
          translate: { x: -15, y: -15 },
          path: [
            { x: x, y: 0 },
            {
              arc: [
                {
                  x: x,
                  y: 15,
                  z: z,
                },
                { x: x, y: 30, z: 0 },
              ],
            },
          ],
          closed: false,
          color: colorCycle(x),
        });
      }
    }

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

customElements.define("cushion-model", CushionModel);
