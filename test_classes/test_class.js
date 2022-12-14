/**
 * this.layout is a builder (look at the builder pattern) which is used to build layout objects
 * in plotly javascript.
 */
 export default class LayoutBuilder {
  /**
   * a layoutBuilder cna be used to build the layout object, this.layout can then be
   * initialised using the ``buildLayout()`` method
   * @param {*} title - this refers to the title of the plot
   */
  constructor(title) {
    this.layout = {};
    this.layout.title = title;
  }

  /**
   * this.layout is a private internal method used to update properties of the layout object
   * @param {*} axis - this is the axis x, y, z
   * @param {*} key - this is the property which needs to be targeted
   * @param {*} value - this is the value which needs to be assigned
   * @returns this.layout
   */
  updateAxis = (axis, key, value) => {
    this.layout["yaxis"] =
      this.layout.yaxis === undefined ? {} : this.layout.yaxis;
    this.layout["xaxis"] =
      this.layout.xaxis === undefined ? {} : this.layout.xaxis;
    this.layout["scene"] =
      this.layout.scene === undefined ? { zaxis: [] } : this.layout.scene;

    if (axis === "y") {
      this.layout["yaxis"][`${key}`] = value;
    } else if (axis === "x") {
      this.layout["xaxis"][`${key}`] = value;
    } else {
      this.layout.scene = {
        xaxis: this.layout["xaxis"],
        yaxis: this.layout["yaxis"],
        zaxis: [],
      };
      this.layout.scene["zaxis"][`${key}`] = value;
    }
    return this;
  };

  /**
   * this.layout will change font o the plot
   * @param {*} color - this changes the color of the plot
   * @param {*} family - this changes the font family typicaly "Arial, sans-serif"
   * @param {*} size - this changes the font size typically 18
   * @returns this.layout
   */
  styleFont = (color, family, size) => {
    this.layout.font = {
      color,
      family,
      size,
    };
    return this;
  };

  /**
   * this.layout will change the background color of the paper and the plot
   * @param {*} paperColor - this changes the color of the plot image
   * @param {*} plotBgColor - this changes the background color of the lot
   * @returns this.layout
   */
  styleBgColor = (paperColor, plotBgColor) => {
    this.layout.paper_bgcolor = paperColor;
    this.layout.plot_bgcolor = plotBgColor;
    return this;
  };

  /**
   * this.layout can be used to add a grid to the desired axis and add color
   * @param {*} gridcolor - this is the color of the grid line
   * @param {*} axis - this is the desired axis
   * @returns this.layout
   */
  addGrid = (gridcolor, axis) => {
    this.updateAxis(axis, "gridcolor", gridcolor);
    return this;
  };

  /**
   * this.layout can be used to style the x or the y axis
   * @param {*} showline - boolean can be true or false
   * @param {*} gridwidth - number typically 1
   * @param {*} showgrid - boolean can be true or false
   * @param {*} zerolinewidth - number typically 2
   * @param {*} autorange - boolean can be true or false
   * @returns this.layout
   */
  styleAxis = (
    axis,
    showline,
    gridwidth,
    showgrid,
    zerolinewidth,
    autorange
  ) => {
    this.updateAxis(axis, "showline", showline);
    this.updateAxis(axis, "gridwidth", gridwidth);
    this.updateAxis(axis, "showgrid", showgrid);
    this.updateAxis(axis, "zerolinewidth", zerolinewidth);
    this.updateAxis(axis, "autorange", autorange);
    return this;
  };

  /**
   * this.layout can be used to style the text of the axis
   * @param {*} family - font family of the axis being styled typically "Arial, sans-serif"
   * @param {*} size - font size of the axis typically 18
   * @param {*} color - color of the text of the axis
   * @returns this.layout
   */
  styleAxisFont = (axis, data, family, size, color) => {
    this.layout.data = {
      family,
      size,
      color,
    };
    this.updateAxis(axis, "titlefont", data);
    return this;
  };

  /**
   * this.layout will add the label to the desired axis
   * @param {*} title - this is the name of the axis
   * @param {*} axis - this is the selected axis
   * @returns this.layout
   */
  addAxis = (axis, title) => {
    this.updateAxis(axis, "title", title);
    return this;
  };

  /**
   * this.layout can be used to change the axis to a log scale
   * @param {*} axis - this can be x , y ,z
   * @returns this.layout
   */
  addLogScale = (axis) => {
    this.updateAxis(axis, "type", "log");
    return this;
  };

  /**
   * add the following object:
   * ```javascript
   * layout : {
   *  autosize : true;
   *  margin : {
   *    l: 0,
   *    r: 0,
   *    b: 30,
   *    t: 0,
   *  }
   * }
   * ```
   * @returns this
   */
  add3DStyles = () => {
    this.layout = {
      ...this.layout,
      autosize: true,
      margin: {
        l: 0,
        r: 0,
        b: 30,
        t: 30,
      },
    };
    return this;
  };

  /**
   * this.layout will add a margin object to he body of the layout object
   * @param {*} l - this
   * @param {*} r - this
   * @param {*} b - this
   * @param {*} t - this
   * @param {*} pad - this
   * @returns ths
   */
  addMargin = (l, r, b, t, pad) => {
    this.layout.margin = {
      l,
      r,
      b,
      t,
      pad,
    };
    return this;
  };

  /**
   * this.layout removes the grid in a particular direction by adding ``showgrid : false``
   * @param {*} axis - this is the axis you want to remove the grid for
   * @returns
   */
  removeGrid = (axis) => {
    this.updateAxis(axis, "shogrid", false);
    return this;
  };

  /**
   * add ``zeroline : false`` to the selected axis object
   * @params axis - this is the axis that will be applied the transformation too
   * @returns this.layout
   */
  removeZeroLine = (axis) => {
    this.updateAxis(axis, "zeroline", false);
    return this;
  };

  addZeroLine = (axis, color) => {
    this.updateAxis(axis, "zeroline", true);
    this.updateAxis(axis, "zerolinecolor", color);
    return this;
  };

  /**
   * this.layout adds a legend by adding the following object to the body
   * of the layout:
   * ```javascript
   * legend : {
   *   width : 500,
   *   height : 500,
   *   y : 0.5,
   *   yref : "paper",
   *   font : {
   *   family : "Arial, sans-serif",
   *   size : 20,
   *   color : "black"
   *  },
   * }
   * ```
   * @returns this.layout
   */
  addLegend = () => {
    this.layout.legend = {
      width: 500,
      height: 500,
      y: 0.5,
      yref: "paper",
      font: {
        family: "Arial, sans-serif",
        size: 20,
        color: "black",
      },
    };
    return this;
  };

  /**
   * this.layout can be used to change the configuration of the bar charts
   * @param {*} barmode - this can be "stack" or "group"
   * @returns this.layout
   */
  styleBarChart = (barmode) => {
    this.layout.barmode = barmode;
    this.layout.bargap = 0.15;
    this.layout.bargroupgap = 0.1;
    return this;
  };

  /**
   * this.layout can be used to change the configuration of histograms
   * @param {*} barmode - this can be "stack" or "overlay"
   * @returns this.layout
   */
  styleHistograms = (barmode) => {
    this.layout.barmode = barmode;
    return this;
  };

  /**
   * this.layout can be used to group box plots
   * this.layout will return ``boxmode : "group"``
   * @returns this.layout
   */
  styleBoxPlot = () => {
    this.layout.boxmode = "group";
    return this;
  };

  addTitle = (title) => {
    this.layout.title = title;
    return this;
  };

  /**
   * this.layout can be used when an existing layout has to be extended
   * @param {*} layout - this is an existing layout object
   * @returns
   */
  addLayoutData = (layout) => {
    this.layout = layout;
    return this;
  };

  /**
   * this.layout is used to return the find body of the layout
   * @returns this.layout
   */
  buildLayout = () => {
    return this.layout;
  };
}
