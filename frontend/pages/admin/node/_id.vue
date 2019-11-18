<template>
  <div>
    <div class="show-data col-xl-12 order-xl-1">
      <div class="card shadow bg-secondary">
        <div class="card-header">
          <div class="bg-white border-0">
            <div class="row align-items-center">
              <div class="col-8">
                <h3 class="mb-0">
                  Add New Node
                </h3>
              </div>
            </div>
          </div>
        </div><div class="card-body">
          <form>
            <h6 class="heading-small text-muted mb-4">
              Node information
            </h6>
            <div class="pl-lg-4">
              <div class="row">
                <div class="col-lg-4">
                  <div class="form-group has-label">
                    <label class="form-control-label">
                      Name
                    </label>
                    <input
                      v-model="data.name"
                      type="text"
                      aria-describedby="addon-right addon-left"
                      alternative=""
                      placeholder="name"
                      class="form-control form-control-alternative"
                    >
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-6">
                  <div class="form-group has-label">
                    <label class="form-control-label">
                      Address
                    </label>
                    <input
                      v-model="data.address"
                      type="text"
                      aria-describedby="addon-right addon-left"
                      alternative=""
                      placeholder="address"
                      class="form-control form-control-alternative"
                    >
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-lg-3">
                  <div class="form-group has-label">
                    <label class="form-control-label">
                      Lat
                    </label>
                    <input
                      v-model="data.lat"
                      type="number"
                      aria-describedby="addon-right addon-left"
                      alternative=""
                      placeholder="Latitude"
                      class="form-control form-control-alternative"
                    >
                  </div>
                </div><div class="col-lg-3">
                  <div class="form-group has-label">
                    <label class="form-control-label">
                      Long
                    </label>
                    <input
                      v-model="data.long"
                      type="number"
                      aria-describedby="addon-right addon-left"
                      alternative=""
                      placeholder="Longitude"
                      class="form-control form-control-alternative"
                    >
                  </div>
                </div>
              </div>
            </div>
            <hr class="my-4">
            <h6 class="heading-small text-muted mb-4">
              Manager information
            </h6>
            <div class="pl-lg-4">
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group has-label">
                    <label class="form-control-label">
                      Manager
                    </label>
                    <input
                      v-model="data.manager"
                      type="text"
                      aria-describedby="addon-right addon-left"
                      alternative=""
                      placeholder="Name manager"
                      class="form-control form-control-alternative"
                    >
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="offset-md-10 col-md-2">
                  <base-button type="default" @click="editNode">
                    Edit Node
                  </base-button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  layout: 'DashboardLayout',
  middleware: ['auth'],
  data () {
    return {
      data: {
        name: '',
        address: '',
        lat: '',
        long: '',
        manager: '',
        key: ''
      }
    }
  },
  async created () {
    const rawData = await this.$axios.$get(`/api/node/${this.$route.params.id}`)
    this.data = rawData.data
  },
  methods: {
    async registerNode () {
      this.$nuxt.$loading.start()
      const params = {
        name: this.name,
        address: this.address,
        lat: this.lat,
        long: this.long,
        manager: this.manager
      }
      await this.$store.dispatch('node/registerNode', params)
      this.$nuxt.$loading.finish()
    },
    async editNode () {
      this.$nuxt.$loading.start()
      const params = {
        id: this.$route.params.id,
        name: this.data.name,
        address: this.data.address,
        lat: this.data.lat,
        long: this.data.long,
        manager: this.data.manager
      }
      await this.$store.dispatch('node/editNode', params)
      this.$nuxt.$loading.finish()
    }

  }
}
</script>
<style lang="scss" scoped>
.show-data {
  margin-top: 1em;
}
</style>
