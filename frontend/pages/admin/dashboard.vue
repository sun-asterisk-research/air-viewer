<template>
  <div />
</template>
<script>
export default {
  layout: 'DashboardLayout',
  middleware: ['auth'],
  data () {
    return {
      node: {}
    }
  },
  // created() {
  //   console.log()
  // },
  async created () {
    const nodes = await this.$axios.$get('/api/node/public')
    this.node = nodes
  }
}
</script>
<style>
</style>
