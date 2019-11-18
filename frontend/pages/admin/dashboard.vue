<template>
  <div />
</template>
<script>
import Hero from '~/components/argon-demo/Hero'
import Logo from '~/components/Logo.vue'
export default {
  layout: 'DashboardLayout',
  components: {
    Hero,
    Logo
  },
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
