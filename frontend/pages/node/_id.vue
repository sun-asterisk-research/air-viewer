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
        <div class="container shape-container d-flex mt-20">
          <div class="col px-0">
            <div class="row justify-content-between align-items-end">
              <div class="col-lg-8">
                <h2 class="display-3 text-white">
                  Báo cáo khách quan chất lượng không khí
                  <span>được vẽ bằng biểu đồ</span>
                </h2>
                <p class="lead  text-white">
                  Chúng tôi thu thập dữ liệu thực từ các vị trí cảm biến ở {{ data[0].address }}.
                </p>
              </div>
              <div class="col-lg-4">
                <div class="btn-wrapper mb-2">
                  <base-button
                    v-if="daily"
                    class="mb-3 mb-sm-0 ml-auto"
                    type="info"
                    icon="ni ni-bold-down"
                  >
                    24 Giờ
                  </base-button>
                  <base-button
                    v-else
                    class="mb-3 mb-sm-0 ml-auto"
                    type="white"
                    icon="ni ni-bold-right"
                    @click="showDaily"
                  >
                    24 giờ
                  </base-button>
                  <base-button
                    v-if="weekly"
                    class="mb-3 mb-sm-0 ml-auto"
                    type="info"
                    icon="ni ni-bold-down"
                  >
                    7 ngày
                  </base-button>
                  <base-button
                    v-else
                    class="mb-3 mb-sm-0 ml-auto"
                    type="white"
                    icon="ni ni-bold-right"
                    @click="showWeekly"
                  >
                    7 ngày
                  </base-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- 1st Hero Variation -->
    </div>
    <section class="section section-lg pt-lg-0 mt--250">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="row row-grid">
              <div class="col-lg-12">
                <card class="border-0" hover shadow body-classes="py-5">
                  <div v-show="daily" id="chartdaily" />
                  <div v-show="weekly" id="chartweekly" />
                </card>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      daily: true,
      weekly: false
    }
  },
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

    const chart = am4core.create('chartdaily', am4charts.XYChart)
    const chartweekly = am4core.create('chartweekly', am4charts.XYChart)

    chart.hiddenState.properties.opacity = 0 // this creates initial fade-in
    chartweekly.hiddenState.properties.opacity = 0

    chart.data = this.data[0]._24h

    chartweekly.data = this.data[0]._7day

    // daily
    const categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
    categoryAxis.renderer.grid.template.location = 0
    categoryAxis.dataFields.category = 'created_at'
    categoryAxis.renderer.minGridDistance = 40
    categoryAxis.fontSize = 11

    // weekly
    const categoryAxisWeekly = chartweekly.xAxes.push(new am4charts.CategoryAxis())
    categoryAxisWeekly.renderer.grid.template.location = 0
    categoryAxisWeekly.dataFields.category = 'created_at'
    categoryAxisWeekly.renderer.minGridDistance = 40
    categoryAxisWeekly.fontSize = 11

    // daily
    const valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
    // weekly
    const valueAxisweekly = chartweekly.yAxes.push(new am4charts.ValueAxis())

    valueAxis.min = 0
    valueAxisweekly.min = 0

    // daily
    const series = chart.series.push(new am4charts.ColumnSeries())
    series.dataFields.categoryX = 'created_at'
    series.dataFields.valueY = 'aqi'
    series.columns.template.tooltipText = '{valueY.value}'
    series.columns.template.tooltipY = 0
    series.columns.template.strokeOpacity = 0

    // weekly
    const seriesweekly = chartweekly.series.push(new am4charts.ColumnSeries())
    seriesweekly.dataFields.categoryX = 'created_at'
    seriesweekly.dataFields.valueY = 'aqi'
    seriesweekly.columns.template.tooltipText = '{valueY.value}'
    seriesweekly.columns.template.tooltipY = 0
    seriesweekly.columns.template.strokeOpacity = 0

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

    seriesweekly.columns.template.adapter.add('fill', function (fill, target) {
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
    this.chartweekly = chartweekly
  },
  beforeDestroy () {
    if (this.chart) {
      this.chart.dispose()
    }
    if (this.chartweekly) {
      this.chartweekly.dispose()
    }
  },
  methods: {
    showDaily () {
      this.daily = true
      this.weekly = false
    },
    showWeekly () {
      this.daily = false
      this.weekly = true
    }
  }
}
</script>

<style lang="scss" scoped>
#chartdaily {
  height: 500px;
}
#chartweekly {
  height: 500px;
}
.mt-20 {
  margin-top: -5em;
}
.mt--10 {
  margin-top: -10px;
}
.mt--250 {
  margin-top: -270px;
}
</style>
