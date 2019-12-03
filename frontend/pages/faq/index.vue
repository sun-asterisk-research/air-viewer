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
                  <h1>FAQs</h1>
                </div>
                <div class="text-muted mb-3">
                  Các câu hỏi thường gặp
                </div>
                <dt class="mb-3">
                  Chỉ số AQI là gì?
                </dt>
                <div class="mb-3">
                  <nuxt-link to="/faq/aqi">
                    Chi tiết của chỉ số AQI.
                  </nuxt-link>
                </div>
                <br>
                <dt class="mb-3">
                  Ai đã tạo ra dịch vụ này?
                </dt>
                <div class="mb-3">
                  Đơn giản, chúng tôi làm vì niềm vui.
                </div>
                <br>
                <dt class="mb-3">
                  Dịch vụ Air Viewer này hoạt động như thế nào?
                </dt>
                <div class="mb-3">
                  Chúng tôi sử dụng Nova PM sensor SDS011 để đo chất lượng không khí. Sensor này sử dụng Lase để đo nên tính chính xác khá cao. Kết quả được xử lý tại thiết bị Rasberry Pi, và sau đó được đẩy lên hiển thị tại server.
                  Các bạn có thể xem thêm hướng dẫn về cách tự thiết lập một bộ thiết bị đo chất lượng không khí tại nhà thông qua <a href="https://viblo.asia/p/tu-do-chi-so-o-nhiem-khong-khi-tai-nha-voi-sensor-va-raspberry-pi-YWOZrBBvZQ0" target="_blank">bài viết này</a>.
                  Toàn bộ source code của dự án được public tại <a href="https://github.com/sun-asterisk-research/air-viewer" target="_blank">https://github.com/sun-asterisk-research/air-viewer</a>.
                </div>
                <br>
                <dt class="mb-3">
                  Thông số của các bạn đưa ra có chính xác không?
                </dt>
                <div class="mb-3">
                  Thông số được hiển thị tại Air Viewer là kết quả được lấy trực tiếp từ sensor. Chúng tôi không hề can thiệp hay chỉnh sửa.
                  Còn chính xác hay không thì phụ thuộc vào thiết bị nữa.
                </div>
                <br>
                <dt class="mb-3">
                  Tôi đã tự làm được một bộ thiết bị đo chất lượng không khí ở nhà rồi, giờ tôi muốn đóng góp dữ liệu cho hệ thống thì phải làm thế nào?
                </dt>
                <div class="mb-3">
                  Do rất khó để kiểm soát độ chính xác của dữ liệu submit từ phía client lên, thế nên hiện tại chúng tôi chỉ cho phép các Node (các thiết bị) của các thành viên trong nhóm, những người mà chúng tôi thực sự tin tưởng, join vào và gửi dữ liệu lên hệ thống.
                  Chính vì thế, bước đầu tiên bạn cần làm đó là trở thành một thành viên của Sun* R&D. Hãy bắt đầu ngay <a href=" https://research.sun-asterisk.com/en/join-us" target="_blank">tại đây</a> nhé.
                </div>
                <br>
                <dt class="mb-3">
                  Tôi thấy chỉ số không khí đang cao, chứng tỏ chất lượng không khí kém quá. Các bạn có thể giảm nó xuống, để không khí bớt ô nhiễm đi được không?
                </dt>
                <div class="mb-3">
                  Xin lỗi, ở đây chúng tôi không làm thế.
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
