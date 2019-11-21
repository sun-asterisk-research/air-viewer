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
                  <h1>What is AQI?</h1>
                </div>
                <div class="text-muted mb-3">
                  Guide to understanding the Air Quality Index
                </div>
                <div class="mb-3">
                  AQI, or Air Quality Index, is a system for translating sometimes confusing or unintuitive pollutant concentration measurements, into one easy-to-understand scale to clearly represent the health risk posed by ambient air pollution. The index formula usually considers up to 6 main pollutants (PM2.5, PM10, carbon monoxide, sulfur dioxide, nitrogen dioxide and ground level ozone), and calculates the respective health risk (or AQI number) for each one at any given time. The overall AQI number at a given moment is dictated by the "riskiest" pollutant, with the highest AQI number.
                </div>
                <div class="mb-3">
                  The index ranges from 0 to 500, where high index values indicate higher levels of air pollution and higher potential for adverse health effects. Any value larger than 300, for example, is considered to be hazardous, while an AQI value of 0-50, on the other hand, represents good air quality.
                </div>
                <div class="mb-3">
                  AQI is computed in different ways around the world. China and America have the two most widely used systems. Both are calculated weighting the six key pollutants. The results of these two functions differ only in AQI scores of 200 and below.
                </div>
                <div class="mb-3">
                  Since the American index system yields higher scores for AQI’s under 200, it is thought to be more strenuous. For this reason, the American index has become the general world standard.
                </div>
                <div class="mb-3">
                  AirVisual uses the US EPA National Ambient Air Quality Standards to calculate AQI and attribute code color. Both US and Chinese AQI systems are available on the AirVisual app and Node.
                </div>
                <div class="mb-3">
                  The standards are as follows:
                </div>
                <dt class="mb-3">
                  0-50, “Good”
                </dt>
                <div class="mb-3">
                  Air quality is satisfactory and poses little or no health risk. Ventilating your home is recommended.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  Enjoy your usual outdoor activities. We recommend opening your windows and ventilating your home to bring in fresh, oxygen-rich air.
                </div>
                <dt class="mb-3">
                  51-100, “Moderate”
                </dt>
                <div class="mb-3">
                  Air quality is acceptable and poses little health risk. Sensitive individuals should avoid outdoor activity as they may experience respiratory symptoms.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  Sensitive groups should greatly reduce outdoor exercise. Ventilation is discouraged, and windows should be closed to avoid dirty outdoor air.
                </div>
                <dt class="mb-3">
                  101-150, “Unhealthy for Sensitive Groups”
                </dt>
                <div class="mb-3">
                  General public and sensitive individuals in particular are at risk to experience irritation and respiratory problems.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  The general public should greatly reduce outdoor exertion. Sensitive groups should avoid all outdoor activity and should take care to wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on if indoor air quality is unhealthy.
                </div>
                <dt class="mb-3">
                  151-200, “Unhealthy”
                </dt>
                <div class="mb-3">
                  Increased likelihood of adverse effects and aggravation to the heart and lungs among general public - particularly for sensitive groups.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  Everyone should avoid outdoor exercise and take care to wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.
                </div>
                <dt class="mb-3">
                  201-300, “Very Unhealthy”
                </dt>
                <div class="mb-3">
                  General public will be noticeably affected. Sensitive groups will experience reduced endurance in activities. These individuals should remain indoors and restrict activities.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  Everyone should avoid outdoor exercise and take care to wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.
                </div>
                <dt class="mb-3">
                  301-500+, “Hazardous”
                </dt>
                <div class="mb-3">
                  General public and sensitive groups are at high risk to experience strong irritations and adverse health effects that could trigger other illnesses. Everyone should avoid exercise and remain indoors.
                </div>
                <dt class="mb-3">
                  <em>Recommendations</em>
                </dt>
                <div class="mb-3">
                  Everyone should avoid outdoor exercise and take care to wear a pollution mask outdoors. Ventilation is discouraged. Air purifiers should be turned on.
                </div>
                <div class="mb-3">
                  <em>
                    **Sensitive groups include children, elderly and pregnant people or those suffering from cardiac or pulmonary diseases.
                  </em>
                </div>
                <div>
                  <img style="max-width: 100%;" src="https://downloads.intercomcdn.com/i/o/159422201/20251ea4a1017f9c8967192f/AQI+guide.png">
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
