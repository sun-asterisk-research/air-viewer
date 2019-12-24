<template>
  <div>
    <client-only>
      <hero>
        <div class="mt-3 mb-5">
          <el-table
            v-if="widthScreen <= 700"
            :data="nodes"
            style="width: 100%"
            :row-class-name="tableRowClassName"
            class="mobile h-50 source"
            :cell-style="{padding: '20'}"
          >
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-card :body-style="{ padding: '0px' }">
                  <b-embed
                    type="iframe"
                    aspect="16by9"
                    :class="`mapGoogle`"
                    :src="
                      `https://maps.google.com/maps?amp;hl=en&amp;q=${props.row.address}+(My%20Business%20Name)&amp;ie=UTF8&amp;t=&amp;z=14&amp;iwloc=B&amp;output=embed`
                    "
                  />
                  <div style="padding: 14px 9px;">
                    <div class="row">
                      <div class="col-6 ">
                        <span class="el-tag el-tag--danger el-tag--dark float-left font-10px-sc320">
                          PM2.5 | {{ props.row.data.pm25 }} µg/m³
                        </span>
                      </div>
                      <div class="col-6 ">
                        <span class="el-tag el-tag--warning el-tag--dark float-right font-10px-sc320">
                          PM10 | {{ props.row.data.pm10 }} µg/m³
                        </span>
                      </div>
                    </div>
                  </div>
                </el-card>
                <div class="mx-auto mt-3" style="width:30%">
                  <el-button type="primary" round size="mini" @click="detailNode(props.row)">
                    {{ $t('home.slide.detail') }}
                  </el-button>
                </div>
              </template>
            </el-table-column>
            <el-table-column
              label="Address"
              prop="address"
              align="center"
            >
              <template slot-scope="props">
                <p :id="`index-${props.row.id}`">
                  {{ props.row.address }}
                </p>
              </template>
            </el-table-column>
            <el-table-column
              label="AQI"
              align="center"
            >
              <template slot-scope="props" width="100px">
                <b-card-text
                  class="card__status-data font-aqi-mobile pt-3"
                  :class="['color-' + props.row.data.status.type]"
                >
                  {{ props.row.data.aqi }}
                </b-card-text>
                <img v-if="props.row.id - 1 !== indexPin" class="icon-pin-mobile" src="/pin plus.png" @click="pinHome(props.row.id)">
                <img v-if="props.row.id - 1 === indexPin" class="icon-pin-mobile" src="/754604.png" @click="unPinHome(props.row.id)">
              </template>
            </el-table-column>
          </el-table>

          <carousel-3d
            v-else
            :start-index="indexPin ? indexPin : 0 "
            :height="620"
            :width="600"
            :border="1"
            :perspective="5"
            :space="620"
            dir="ltr"
            class="desktop"
          >
            <slide v-for="(node, i) in nodes" :key="i" :index="i" class="slide">
              <div>
                <b-card class="text-center box-shadow" :class="['card-' + node.data.status.type]">
                  <b-card-title style="height: 2.5em;">
                    <img v-if="node.id - 1 !== indexPin" class="icon-pin-desktop" src="/pin plus.png" @click="pinHome(node.id)">
                    <img v-if="node.id - 1 === indexPin" class="icon-pin-desktop" src="/754604.png" @click="unPinHome(node.id)">
                    <span>{{ node.address }}</span>
                  </b-card-title>

                  <b-card-text
                    class="card__status-data"
                    style="margin:0 auto; width:85%;"
                  >
                    <b-embed
                      type="iframe"
                      aspect="16by9"
                      :class="`mapGoogle`"
                      :src="
                        `https://maps.google.com/maps?amp;hl=en&amp;q=${node.address}+(My%20Business%20Name)&amp;ie=UTF8&amp;t=&amp;z=14&amp;iwloc=B&amp;output=embed`
                      "
                    />
                  </b-card-text>

                  <b-card-text
                    v-if="$i18n.locale === 'vi'"
                    class="card__status"
                    :class="['color-' + node.data.status.type]"
                  >
                    {{ node.data.status.info }}
                  </b-card-text>
                  <b-card-text
                    v-else
                    class="card__status"
                    :class="['color-' + node.data.status.type]"
                  >
                    {{ node.data.status.infoEng }}
                  </b-card-text>

                  <b-card-text
                    class="card__status-data pt-3"
                    :class="['color-' + node.data.status.type]"
                  >
                    {{ node.data.aqi }}
                    <span class="card__status-param">US AQI</span>
                  </b-card-text>

                  <b-card-text
                    class="card__status-info"
                    :class="['color-' + node.data.status.type]"
                  >
                    <span class="card__status-number">PM2.5 | {{ node.data.pm25 }} µg/m³</span>
                    <span class="card__status-number">PM10 | {{ node.data.pm10 }} µg/m³</span>
                  </b-card-text>

                  <b-card-text @click="detailNode(node)">
                    {{ $t('home.slide.detail') }}
                  </b-card-text>
                </b-card>
              </div>
            </slide>
          </carousel-3d>
        </div>
      </hero>
    </client-only>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
const Hero = () => import('~/components/argon-demo/Hero')

export default {
  components: {
    Hero
  },
  data () {
    return {
      indexPin: null,
      widthScreen: 0
    }
  },
  head () {
    return {
      title: 'Sun* Air Viewer',
      meta: [
        { property: 'og:title', content: 'Sun* Air Viewer' },
        {
          property: 'og:description',
          content:
            this.$i18n.locale === 'vi'
              ? 'Thông tin tổng quan chung chất lượng không khí hiện tại'
              : 'General overview of current air quality'
        }
      ]
    }
  },
  computed: {
    ...mapGetters('node', {
      nodes: 'getNodes'
    })
  },
  mounted () {
    if (localStorage.getItem('indexPin')) {
      this.indexPin = localStorage.getItem('indexPin') - 1
      setTimeout(() => {
        this.scrollToDiv(this.indexPin)
      }, 300)
    }
    this.widthScreen = window.screen.width
  },
  methods: {
    detailNode (node) {
      this.$router.push(
        this.$i18n.locale === 'vi'
          ? { path: `/node/${node.id}` }
          : { path: `/en/node/${node.id}` }
      )
    },
    tableRowClassName ({ row, rowIndex }) {
      return ' card-' + row.data.status.type
    },
    toggleDetails (index) {
      this.$store.commit('toggleShowDetails', index)
    },
    pinHome (nodeId) {
      localStorage.setItem('indexPin', nodeId)
      this.indexPin = nodeId - 1
    },
    unPinHome (nodeId) {
      localStorage.removeItem('indexPin')
      this.indexPin = null
    },
    scrollToDiv (nodeId) {
      this.$scrollTo(`#index-${nodeId}`)
    }
  }
}
</script>
<style lang="scss">

.card {
  &-1 {
    background-color: #a8e05f !important;
  }
  &-1:hover {
    background-color: #a8e05f !important;
  }
  &-2 {
    background-color: #fdd74b !important;
  }
  &-3 {
    background-color: #fb9b57 !important;
  }
  &-4 {
    background-color: #fe6a69 !important;
  }
  &-5 {
    background-color: #a97abc !important;
  }
  &-6 {
    background-color: #a87383 !important;
  }
  &__status {
    font-size: 20px;
    font-weight: 600;

    &-data {
      font-size: 104px;
      font-weight: 600;
      line-height: 50px;
    }

    &-param {
      font-size: 12px;
      font-weight: 600;
      line-height: 50px;
    }

    &-info {
      margin-bottom: 20px !important;
    }

    &-number {
      background: #fff;
      border-radius: 5px;
      font-size: 14px;
      font-weight: 500;
      padding: 5px 10px;
    }
  }
}

.color {
  &-1 {
    color: #718b3a;
  }
  &-2 {
    color: #a57f23;
  }
  &-3 {
    color: #b25826;
  }
  &-4 {
    color: #af2c3b;
  }
  &-5 {
    color: #634675;
  }
  &-6 {
    color: #683e51;
  }
}

@media only screen and (max-width: 320px) {
  .font-10px-sc320{
    font-size: 10px;
  }
}

@media only screen and (max-width: 700px) {
  .desktop {
    display: none;
  }
  .cell > p {
    margin-bottom: 0;
    text-align: center;
  }
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.source {
  border-radius: 3px;
  transition: .2s;
  background: #d3dce6;
}

.box-shadow {
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
}

.font-aqi-mobile {
  font-size: 50px;
  font-weight: 600;
  line-height: 50px;
}

.el-table__expanded-cell {
  padding: 20px !important;
}

.icon-pin-desktop {
  width:40px !important;
  float:left;
  clear:both;
}

.icon-pin-mobile {
  width:25px !important;
  float:right;
  clear:both;
}

.el-table--enable-row-hover .el-table__body tr:hover>td {
  background: none;
}

.float-left {
  float: left;
}
.float-right{
  float:right;
}
</style>

<style lang="scss" scoped>
@media only screen and (min-width: 700px) {
  .mobile {
    display: none;
  }
  .card-body {
    height: 620px !important;
    width: 600px !important;
  }
  .slide {
    cursor: pointer;
    border-radius: 25px;
  }
}
</style>
