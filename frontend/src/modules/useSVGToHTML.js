const SVGToHTML = (svg) => {
    const range = document.createRange();
    const fragment = range.createContextualFragment(svg);

    return fragment.firstChild;
};

export default SVGToHTML;