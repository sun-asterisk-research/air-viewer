<template>
  <div>
    <div class="position-relative">
      <!-- shape Hero -->
      <section class="section-shaped my-0">
        <div class="shape shape-style-1 shape-default shape-skew">
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
        </div>
        <div class="container shape-container d-flex">
          <div class="col px-0">
            <div class="row">
              <div class="col-lg-6">
                <h1 class="display-3  text-white">
                  A daily report air visual
                  <span>completed with chart</span>
                </h1>
                <p class="lead  text-white">
                  We collect real data from sensors locations in Hanoi.
                </p>
                <div class="btn-wrapper">
                  <base-button
                    tag="a"
                    href="https://demos.creative-tim.com/argon-design-system/docs/components/alerts.html"
                    class="mb-3 mb-sm-0"
                    type="info"
                    icon="fa fa-code"
                  >
                    Weekly
                  </base-button>
                  <base-button
                    tag="a"
                    href="https://www.creative-tim.com/product/argon-design-system"
                    class="mb-3 mb-sm-0"
                    type="white"
                    icon="ni ni-cloud-download-95"
                  >
                    Download HTML
                  </base-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- 1st Hero Variation -->
    </div>
    <!-- <section class="section section-lg pt-lg-0 mt--200">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="row row-grid">
              <div class="col-lg-12">
                <card class="border-0" hover shadow body-classes="py-5">
                  <icon name="ni ni-check-bold" type="primary" rounded class="mb-4" />
                  <h6 class="text-primary text-uppercase">
                    <div>{{ data }}</div>
                  </h6>
                  <p class="description mt-3">
                    Argon is a great free UI package based on Bootstrap 4
                    that includes the most important components and features.
                  </p>
                  <div>
                    <badge type="primary" rounded>
                      design
                    </badge>
                    <badge type="primary" rounded>
                      system
                    </badge>
                    <badge type="primary" rounded>
                      creative
                    </badge>
                  </div>
                  <base-button tag="a" href="#" type="primary" class="mt-4">
                    Learn more
                  </base-button>
                </card>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section> -->
    <div id="chartdiv" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('node', [
      'nodeDetail'
    ]),
    data () {
      return this.nodeDetail(this.$route.params.id)
    }
  },
  mounted () {
    //  eslint-disable-next-line
    let {am4core, am4charts, am4themes_animated, am4themes_dark} = this.$am4core()
    //  eslint-disable-next-line
    am4core.useTheme(am4themes_animated)

    const chart = am4core.create('chartdiv', am4charts.XYChart)

    chart.hiddenState.properties.opacity = 0 // this creates initial fade-in

    chart.data = [
      {
        time: '0h',
        aqi: 5
      },
      {
        time: '1h',
        aqi: 30
      },
      {
        time: '2h',
        aqi: 100
      },
      {
        time: '3h',
        aqi: 60
      },
      {
        time: '4h',
        aqi: 70
      },
      {
        time: '5h',
        aqi: 150
      },
      {
        time: '6h',
        aqi: 170
      },
      {
        time: '7h',
        aqi: 210
      },
      {
        time: '8h',
        aqi: 200
      },
      {
        time: '9h',
        aqi: 300
      },
      {
        time: '10h',
        aqi: 220
      },
      {
        time: '11h',
        aqi: 110
      },
      {
        time: '12h',
        aqi: 170
      },
      {
        time: '13h',
        aqi: 120
      },
      {
        time: '14h',
        aqi: 270
      },
      {
        time: '15h',
        aqi: 10
      },
      {
        time: '16h',
        aqi: 70
      },
      {
        time: '17h',
        aqi: 90
      },
      {
        time: '18h',
        aqi: 100
      },
      {
        time: '19h',
        aqi: 400
      },
      {
        time: '20h',
        aqi: 10
      },
      {
        time: '21h',
        aqi: 20
      },
      {
        time: '22h',
        aqi: 4
      },
      {
        time: '23h',
        aqi: 151
      }
    ]

    const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
    categoryAxis.renderer.grid.template.location = 0
    categoryAxis.dataFields.category = 'time'
    categoryAxis.renderer.minGridDistance = 40
    categoryAxis.fontSize = 11

    const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())

    chart.colors.list = [
      am4core.color('#845EC2'),
      am4core.color('#D65DB1'),
      am4core.color('#FF6F91'),
      am4core.color('#FF9671'),
      am4core.color('#FFC75F'),
      am4core.color('#F9F871')
    ]

    valueAxis.min = 0
    // valueAxis.max = 1000
    // valueAxis.strictMinMax = true
    // valueAxis.renderer.minGridDistance = 30
    // axis break
    // const axisBreak = valueAxis.axisBreaks.create()
    // axisBreak.startValue = 2100
    // axisBreak.endValue = 22900
    // axisBreak.breakSize = 0.005

    // make break expand on hover
    // const hoverState = axisBreak.states.create('hover')
    // hoverState.properties.breakSize = 1
    // hoverState.properties.opacity = 0.1
    // hoverState.transitionDuration = 1500

    // axisBreak.defaultState.transitionDuration = 1000
    /*
// this is exactly the same, but with events
axisBreak.events.on("over", function() {
  axisBreak.animate(
    [{ property: "breakSize", to: 1 }, { property: "opacity", to: 0.1 }],
    1500,
    am4core.ease.sinOut
  );
});
axisBreak.events.on("out", function() {
  axisBreak.animate(
    [{ property: "breakSize", to: 0.005 }, { property: "opacity", to: 1 }],
    1000,
    am4core.ease.quadOut
  );
}); */

    const series = chart.series.push(new am4charts.ColumnSeries())
    series.dataFields.categoryX = 'time'
    series.dataFields.valueY = 'aqi'
    series.columns.template.tooltipText = '{valueY.value}'
    series.columns.template.tooltipY = 0
    series.columns.template.strokeOpacity = 0

    // as by default columns of the same series are of the same color, we add adapter which takes colors from chart.colors color set
    series.columns.template.adapter.add('fill', function (fill, target) {
      if (target.dataItem && (target.dataItem.valueY <= 50)) {
        return am4core.color('#A8E05F')
      } else if (target.dataItem.valueY <= 100) {
        return am4core.color('#FDD74B')
      } else if (target.dataItem.valueY <= 150) {
        return am4core.color('#FB9B57')
      } else if (target.dataItem.valueY <= 200) {
        return am4core.color('#fe6a69')
      } else if (target.dataItem.valueY <= 300) {
        return am4core.color('#a97abc')
      } else {
        return am4core.color('#a87383')
      }
      // return chart.colors.getIndex(target.dataItem.index)
    })

    this.chart = chart
  },
  beforeDestroy () {
    if (this.chart) {
      this.chart.dispose()
    }
  }
}
</script>

<style lang="scss" scoped>
#chartdiv {
  height: 500px;
}
</style>
