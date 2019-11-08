<template>
  <div class="row">
    <div class="col-lg-6">
      <small class="d-block text-uppercase font-weight-bold mb-3">Tooltips</small>
      <base-button
        v-b-tooltip.hover.left
        size="sm"
        type="primary"
        class="btn-tooltip"
        title="Tooltip on left"
      >
        On left
      </base-button>
      <base-button
        v-b-tooltip.hover.top
        size="sm"
        type="primary"
        class="btn-tooltip"
        title="Tooltip on top"
      >
        On top
      </base-button>
      <base-button
        v-b-tooltip.hover.bottom
        size="sm"
        type="primary"
        class="btn-tooltip"
        title="Tooltip on bottom"
      >
        On bottom
      </base-button>
      <base-button
        v-b-tooltip.hover.right
        size="sm"
        type="primary"
        class="btn-tooltip"
        title="Tooltip on right"
      >
        On right
      </base-button>
    </div>
    <div class="col-lg-6 mt-4 mt-lg-0">
      <small class="d-block text-uppercase font-weight-bold mb-3">Popovers</small>
      <base-button
        v-b-popover.hover.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"
        size="sm"
        type="default"
        title="Popover On Left"
      >
        On left
      </base-button>

      <base-button
        v-b-popover.hover.left="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"
        size="sm"
        type="default"
        title="Popover On Left"
      >
        On left
      </base-button>

      <base-button
        v-b-popover.hover.top="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"
        size="sm"
        type="default"
        title="Popover On Top"
      >
        On top
      </base-button>
      <base-button
        v-b-popover.hover.right="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"
        size="sm"
        type="default"
        title="Popover On right"
      >
        On right
      </base-button>
      <base-button
        v-b-popover.hover.bottom="'Vivamus sagittis lacus vel augue laoreet rutrum faucibus.'"
        size="sm"
        type="default"
        title="Popover On bottom"
      >
        On bottom
      </base-button>
    </div>
  </div>
</template>
<script>
export default {
}
</script>
