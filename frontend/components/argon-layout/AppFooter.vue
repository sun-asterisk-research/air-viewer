<template>
  <footer class="footer has-cards">
    <div class="container">
      <div class="row row-grid align-items-center my-md">
        <div class="col-lg-6">
          <h3 class="text-primary font-weight-light mb-2">
            Thank you for supporting us!
          </h3>
          <h4 class="mb-0 font-weight-light">
            Let's get in touch on any of these platforms.
          </h4>
        </div>
        <div class="col-lg-6 text-lg-center btn-wrapper">
          <a
            target="_blank"
            rel="noopener"
            href="https://twitter.com/hashtag/sunasterisk"
            class="btn btn-neutral btn-icon-only btn-twitter btn-round btn-lg"
            data-toggle="tooltip"
            data-original-title="Follow us"
          >
            <i class="fab fa-twitter" />
          </a>
          <a
            target="_blank"
            rel="noopener"
            href="https://www.facebook.com/SunAsteriskVietnam"
            class="btn btn-neutral btn-icon-only btn-facebook btn-round btn-lg"
            data-toggle="tooltip"
            data-original-title="Like us"
          >
            <i class="fab fa-facebook-square" />
          </a>
          <a
            target="_blank"
            rel="noopener"
            href="https://github.com/sun-asterisk-research"
            class="btn btn-neutral btn-icon-only btn-github btn-round btn-lg"
            data-toggle="tooltip"
            data-original-title="Star on Github"
          >
            <i class="fab fa-github" />
          </a>
        </div>
      </div>
      <hr>
      <div class="row align-items-center justify-content-md-between">
        <div class="col-md-6">
          <div class="copyright">
            &copy; {{ year }}
            <a href="#" target="_blank" rel="noopener">Sun*</a> & <a href="#" target="_blank" rel="noopener">R&D Research</a>
          </div>
        </div>
        <div class="col-md-6">
          <ul class="nav nav-footer justify-content-end">
            <li class="nav-item">
              <a href="#" class="nav-link" target="_blank" rel="noopener">Sun*</a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" target="_blank" rel="noopener">About
                Us</a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" target="_blank" rel="noopener">Blog</a>
            </li>
            <li class="nav-item">
              <a
                href="#"
                class="nav-link"
                target="_blank"
                rel="noopener"
              >MIT License</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: 'AppFooter',
  data () {
    return {
      year: new Date().getFullYear()
    }
  }
}
</script>
<style>
</style>
