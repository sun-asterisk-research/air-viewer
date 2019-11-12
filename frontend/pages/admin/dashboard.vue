<template>
  <div>
    <hero>
      <div class="mt-4 mb-5">
        <logo />
        <p class="lead text-white">
          Sun* Air Visual project
        </p>
        <p>{node}</p>
      </div>
    </hero>
  </div>
</template>
<script>
import Hero from '~/components/argon-demo/Hero'
import Logo from '~/components/Logo.vue'
export default {
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
