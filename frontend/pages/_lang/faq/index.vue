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
                  <h1>{{ $t('faq.title') }}</h1>
                </div>
                <div class="text-muted mb-3">
                  {{ $t('faq.list') }}
                </div>
                <dt class="mb-3">
                  {{ $t('faq.what_aqi.title') }}
                </dt>
                <div class="mb-3">
                  <nuxt-link :to="$i18n.path('faq/aqi')">
                    {{ $t('faq.what_aqi.link') }}
                  </nuxt-link>
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques1.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques1.answer') }}
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques2.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques2.answer') }}
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques3.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques3.answer') }} <a href="https://viblo.asia/p/tu-do-chi-so-o-nhiem-khong-khi-tai-nha-voi-sensor-va-raspberry-pi-YWOZrBBvZQ0" target="_blank">{{ $t('faq.ques3.link') }}</a>.
                  {{ $t('faq.ques3.answer2') }} <a href="https://github.com/sun-asterisk-research/air-viewer" target="_blank">https://github.com/sun-asterisk-research/air-viewer</a>.
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques4.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques4.answer') }}
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques5.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques5.answer') }} <a href=" https://research.sun-asterisk.com/en/join-us" target="_blank">{{ $t('faq.ques5.link') }}</a>.
                </div>
                <br>
                <dt class="mb-3">
                  {{ $t('faq.ques6.title') }}
                </dt>
                <div class="mb-3">
                  {{ $t('faq.ques6.answer') }}
                </div>
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
