<template>
  <div class="row row-grid justify-content-between align-items-center mt-lg">
    <div class="col-lg-5">
      <h3 class="h4 text-success font-weight-bold mb-4">
        Progress bars
      </h3>
      <base-progress :value="40" label="Task completed" />
      <base-progress type="primary" :value="60" label="Task completed" />
    </div>
    <div class="col-lg-5">
      <h3 class="h4 text-success font-weight-bold mb-5">
        Pagination
      </h3>
      <base-pagination v-model="pagination.default" :page-count="10" />
      <base-pagination v-model="pagination.danger" :page-count="10" />
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      pagination: {
        default: 1,
        danger: 3
      }
    }
  }
}
</script>
<style>
</style>
