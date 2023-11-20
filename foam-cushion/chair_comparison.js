class ChairComparison extends HTMLElement {
  constructor() {
    super();
    this.root = this.attachShadow({ mode: "closed" });
  }
  connectedCallback() {
    this.render();
  }

  render() {
    // in pure html:
    //
    // <div class="juxtapose">
    //   <img src="./images/chair_uncomfy.jpg" />
    //   <img src="./images/chair_comfy.jpg" />
    // </div>
    // <link
    //   rel="stylesheet"
    //   href="https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css"
    // />
    // <script src="https://cdn.knightlab.com/libs/juxtapose/latest/js/juxtapose.min.js"></script>

    const image1src = this.getAttribute("src1");
    const image2src = this.getAttribute("src2");

    const div = document.createElement("div");
    div.setAttribute("id", "slider");
    this.root.appendChild(div);

    let slider = new juxtapose.JXSlider(
      div,
      [
        {
          src: image1src,
        },
        {
          src: image2src,
        },
      ],
      {}
    );

    const link = document.createElement("link");
    link.setAttribute("rel", "stylesheet");
    link.setAttribute(
      "href",
      "https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css"
    );
    this.root.appendChild(link);
  }
}

customElements.define("chair-comparison", ChairComparison);
