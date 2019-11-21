<template>
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
        <div class="col-lg-5">
          <card
            type="secondary"
            shadow
            header-classes="bg-white pb-5"
            body-classes="px-lg-5 py-lg-5"
            class="border-0"
          >
            <!-- <template>
              <div class="text-muted text-center mb-3">
                <small>Sign in with</small>
              </div>
              <div class="btn-wrapper text-center">
                <base-button type="neutral">
                  <img slot="icon" src="/argon/img/icons/common/github.svg">
                  Github
                </base-button>

                <base-button type="neutral">
                  <img slot="icon" src="/argon/img/icons/common/google.svg">
                  Google
                </base-button>
              </div>
            </template> -->
            <template>
              <!-- <div class="text-center text-muted mb-4">
                <small>Or sign in with credentials</small>
              </div> -->
              <form role="form">
                <base-input
                  v-model="username"
                  alternative
                  type="text"
                  class="mb-3"
                  placeholder="Username"
                  addon-left-icon="ni ni-circle-08"
                />
                <base-input
                  v-model="password"
                  alternative
                  type="password"
                  placeholder="Password"
                  addon-left-icon="ni ni-lock-circle-open"
                />
                <!-- <base-checkbox>
                  Remember me
                </base-checkbox> -->
                <div class="text-center">
                  <base-button type="primary" class="my-4" @click="login">
                    Sign In
                  </base-button>
                </div>
              </form>
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
</template>
<script>
export default {
  components: {},
  auth: 'guest',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  watch: {},
  mounted () {},
  methods: {
    google () {},
    facebook () {},
    async login () {
      // await this.$auth.loginWith('local', {
      //   data: {
      //     'username': this.username,
      //     'password': this.password
      //   }
      // }).catch((e) => {
      //   this.$toast.error('Failed Logging In')
      // })
      try {
        await this.$auth.loginWith('local', {
          data: {
            'username': this.username,
            'password': this.password
          }
        }).catch((e) => {
          this.$toast.error('Failed Logging In')
        })
        if (this.$auth.loggedIn) {
          this.$toast.success('Successfully Logged In')
          this.$router.push('/admin/dashboard')
        }
      } catch (e) {
        this.$toast.error('Username or Password wrong')
      }
    },
    logout () {},
    check () {}
  }
}
</script>
<style>
</style>
