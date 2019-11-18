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
  }
}
</script>
<style>
</style>
