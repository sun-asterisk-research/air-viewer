<template>
  <div>
    <client-only>
      <hero>
        <div class="mt-3 mb-5">
          <b-carousel
            indicators
            :interval="5000"
            class="mobile h-50"
          >
            <b-carousel-slide v-for="node in nodes" :key="node.id" class="slide">
              <template slot="img">
                <b-card class="text-center" :class="['card-' + node.data.status.type]" @click="detailNode(node)">
                  <b-card-title>
                    <i class="ni ni-compass-04" />
                    <span>{{ node.address }}</span>
                  </b-card-title>
                  <b-card-text class="card__status" :class="['color-' + node.data.status.type]">
                    {{ node.data.status.info }}
                  </b-card-text>
                  <b-card-text class="card__status-data" :class="['color-' + node.data.status.type]">
                    {{ node.data.aqi }} <span class="card__status-param">US AQI</span>
                  </b-card-text>
                  <b-card-text class="card__status-info" :class="['color-' + node.data.status.type]">
                    <span class="card__status-number">PM2.5 | {{ node.data.pm25 }} µg/m³</span>
                    <span class="card__status-number">PM10 | {{ node.data.pm10 }} µg/m³</span>
                  </b-card-text>
                </b-card>
              </template>
            </b-carousel-slide>
          </b-carousel>
          <carousel-3d
            :height="400"
            :width="600"
            :border="1"
            :perspective="5"
            :autoplay="true"
            :space="620"
            dir="ltr"
            :autoplay-timeout="3000"
            class="desktop"
          >
            <slide v-for="node in nodes" :key="node.id" :index="node.id - 1" class="slide">
              <div>
                <b-card class="text-center" :class="['card-' + node.data.status.type]">
                  <b-card-title style="height: 2.5em;">
                    <i class="ni ni-compass-04" />
                    <span>{{ node.address }}</span>
                  </b-card-title>

                  <b-card-text class="card__status" :class="['color-' + node.data.status.type]">
                    {{ node.data.status.info }}
                  </b-card-text>
                  <b-card-text class="card__status-data pt-3" :class="['color-' + node.data.status.type]">
                    {{ node.data.aqi }} <span class="card__status-param">US AQI</span>
                  </b-card-text>

                  <b-card-text class="card__status-info" :class="['color-' + node.data.status.type]">
                    <span class="card__status-number">PM2.5 | {{ node.data.pm25 }} µg/m³</span>
                    <span class="card__status-number">PM10 | {{ node.data.pm10 }} µg/m³</span>
                  </b-card-text>

                  <b-card-text class="pt-4" @click="detailNode(node)">
                    Thông tin chi tiết
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
  computed: {
    ...mapGetters('node', {
      nodes: 'getNodes'
    })
  },
  methods: {
    detailNode (node) {
      this.$router.push({ path: `/node/${node.id}` })
    }
  }
}
</script>
<style lang="scss" scoped>
.slide {
  cursor: pointer;
}
.card {
  &-1 {
    background-color: #A8E05F;
  }
  &-2 {
    background-color: #FDD74B;
  }
  &-3 {
    background-color: #FB9B57;
  }
  &-4 {
    background-color: #fe6a69;
  }
  &-5 {
    background-color: #a97abc;
  }
  &-6 {
    background-color: #a87383;
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
      margin-bottom: 20px!important;
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

@media only screen and (min-width: 700px) {
  .mobile {
    display: none;
  }
  .card-body {
    height: 400px !important;
    width: 600px !important;
  }
}

@media only screen and (max-width: 700px) {
  .desktop {
    display: none;
  }
}
</style>
