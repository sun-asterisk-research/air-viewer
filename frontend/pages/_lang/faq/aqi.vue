<template>
  <div>
    <section class="section section-shaped section-lg my-0">
      <div class="shape shape-style-1 bg-gradient-default">
        <span />
        <span />
        <span />
        <span />
        <span />
        <span />
        <span />
        <span />
      </div>
      <div class="container pt-lg-md">
        <div class="row justify-content-center">
          <div class="col-lg-10">
            <card
              type="secondary"
              shadow
              header-classes="bg-white pb-5"
              body-classes="px-lg-5 py-lg-5"
              class="border-0"
            >
              <template>
                <div class="mb-3">
                  <h1>{{ $t('aqi.title') }}</h1>
                </div>
                <div class="text-muted mb-3">
                  {{ $t('aqi.span') }}
                </div>
                <div class="mb-3">
                  {{ $t('aqi.p1') }}
                </div>
                <div class="mb-3">
                  {{ $t('aqi.p2') }}
                </div>
                <div class="mb-3">
                  {{ $t('aqi.p3') }}
                </div>
                <div class="mb-3">
                  {{ $t('aqi.p4') }}
                </div>
                <dt class="mb-3">
                  0-50, “{{ $t('aqi.t1.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t1.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t1.text') }}
                </div>
                <br>
                <dt class="mb-3">
                  51-100, “{{ $t('aqi.t2.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t2.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t2.text') }}
                </div>
                <br>
                <dt class="mb-3">
                  101-150, “{{ $t('aqi.t3.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t3.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t3.text') }}
                </div>
                <br>
                <dt class="mb-3">
                  151-200, “{{ $t('aqi.t4.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t4.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t4.title') }}
                </div>
                <br>
                <dt class="mb-3">
                  201-300, “{{ $t('aqi.t5.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t5.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t5.text') }}
                </div>
                <br>
                <dt class="mb-3">
                  301-500+, “{{ $t('aqi.t6.type') }}”
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t6.title') }}
                </div>
                <dt class="mb-3">
                  <em>{{ $t('aqi.recommend') }}</em>
                </dt>
                <div class="mb-3">
                  {{ $t('aqi.t6.text') }}
                </div>
                <br>
                <div class="mb-3">
                  <em>
                    {{ $t('aqi.quote') }}
                  </em>
                </div>
                <!-- <div>
                  <img style="max-width: 100%;" src="https://downloads.intercomcdn.com/i/o/159422201/20251ea4a1017f9c8967192f/AQI+guide.png">
                </div> -->
              </template>
            </card>
            <!-- <div class="row mt-3">
              <div class="col-6">
                <a href="#" class="text-light">
                  <small>Forgot password?</small>
                </a>
              </div>
              <div class="col-6 text-right">
                <a href="#" class="text-light">
                  <small>Create new account</small>
                </a>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {

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
</style>
