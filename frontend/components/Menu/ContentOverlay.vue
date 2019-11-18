<template>
  <div
    class="content-overlay"
    @click.prevent="closeMobileMenu"
  />
</template>

<script>
import { mapActions } from 'vuex'
export default {
  methods: {
    ...mapActions('menu', {
      closeMobileMenu: 'toggle'
    })
  }
}
</script>
<style lang="scss">
.content-overlay {
  position: fixed;
  display: none;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9989;
  pointer-events: auto;
}
</style>
