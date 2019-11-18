<template>
  <div id="wrapper" :class="wrapperClass">
    <MenuToggleBtn />

    <Menu />

    <ContentOverlay />
    <main>
      <nuxt />
    </main>
  </div>
</template>
<script>
import { mapState } from 'vuex'
import MenuToggleBtn from '@/components/Menu/MenuToggleBtn'
import Menu from '@/components/Menu/Menu'
import ContentOverlay from '@/components/Menu/ContentOverlay'

export default {
  components: {
    MenuToggleBtn,
    Menu,
    ContentOverlay
  },
  computed: {
    ...mapState('menu', {
      toggleMenu: 'isOpenMobileMenu'
    }),
    wrapperClass () {
      return {
        'toggled': this.toggleMenu === true
      }
    }
  }
}
</script>
<style lang="scss" scoped>
@import '~/assets/sidebar/layout.scss';
@import '~/assets/sidebar/media-queries.scss';
</style>
