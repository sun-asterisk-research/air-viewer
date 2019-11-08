<template>
  <div>
    <hero>
      <div class="mt-4 mb-5">
        <logo />
        <p class="lead text-white">
          Hello World
        </p>
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
  }
}
</script>
<style>
</style>
