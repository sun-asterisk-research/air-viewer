<template>
  <div id="wrapper" class="d-flex flex-column">
    <header class="header-global">
      <app-header />
    </header>
    <main class="flex-fill position-relative">
      <nuxt />
    </main>
    <footer class="footer">
      <app-footer />
    </footer>
  </div>
</template>

<script>
import AppHeader from '~/components/argon-layout/AppHeader'
import AppFooter from '~/components/argon-layout/AppFooter'

export default {
  components: {
    AppHeader,
    AppFooter
  }
}
</script>

<style>
body, #wrapper {
   min-height:100vh;
}
</style>
