<template>
  <div>
    <div class="show-data col-xl-12 order-xl-1">
      <div class="card shadow bg-secondary">
        <div class="card-header">
          <div class="bg-white border-0">
            <div class="row align-items-center">
              <div class="col-8">
                <h3 class="mb-0">
                  List Nodes
                </h3>
              </div>
            </div>
          </div>
        </div>
        <div class="card-body">
          <b-table striped hover :items="nodes.nodes" :fields="fields">
            <template v-slot:cell(index)="data">
              {{ data.item.id }}
            </template>
            <template v-slot:cell(latlong)="data">
              {{ data.item.lat }}, {{ data.item.long }}
            </template>
            <template v-slot:cell(actions)="data">
              <base-button type="primary" @click="editNode(data.item.id)">
                Edit
              </base-button>
              <base-button type="danger" @click="deleteNode(data.item.id)">
                Delete
              </base-button>
            </template>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  layout: 'DashboardLayout',
  middleware: ['auth'],
  data () {
    return {
      nodes: [],
      fields: [
        // A virtual column that doesn't exist in items
        'index',
        // A column that needs custom formatting
        'name',
        // A regular column
        'address',
        // A regular column
        { key: 'latlong', label: 'Lat, Long' },
        // A virtual column made up from two fields
        'manager',
        'key',
        'actions'
      ]
    }
  },
  async created () {
    this.nodes = await this.$axios.$get('/api/node/private')
  },
  methods: {
    editNode (id) {
      this.$router.push(`/admin/node/${id}`)
    },
    async deleteNode (id) {
      this.$nuxt.$loading.start()
      await this.$store.dispatch('node/deleteNode', id)
      this.nodes = await this.$axios.$get('/api/node/private')
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
