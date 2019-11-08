<template>
  <ul class="navbar-nav ml-lg-auto">
    <li class="nav-item">
      <a class="nav-link nav-link-icon" href="#">
        <i class="ni ni-favourite-28" />
        <span class="nav-link-inner--text d-lg-none">Favorites</span>
      </a>
    </li>
    <li class="nav-item">
      <a class="nav-link nav-link-icon" href="#">
        <i class="ni ni-planet" />
        <span class="nav-link-inner--text d-lg-none">Another action</span>
      </a>
    </li>
    <li class="nav-item dropdown">
      <a
        id="navbar-success_dropdown_1"
        class="nav-link nav-link-icon"
        href="#"
        role="button"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <i class="ni ni-settings-gear-65" />
        <span class="nav-link-inner--text d-lg-none">Settings</span>
      </a>
      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbar-success_dropdown_1">
        <a class="dropdown-item" href="#">Action</a>
        <a class="dropdown-item" href="#">Another action</a>
        <div class="dropdown-divider" />
        <a class="dropdown-item" href="#">Something else here</a>
      </div>
    </li>
  </ul>
</template>
<script>
export default {}
</script>
<style>
</style>
