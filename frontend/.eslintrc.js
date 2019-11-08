module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    '@nuxtjs',
    'plugin:nuxt/recommended'
  ],
  // add your custom rules here
  rules: {
    "vue/require-default-prop": "off",
    "vue/require-prop-types": "off",
    "vue/no-unused-components": "off",
    "vue/no-unused-vars": "off",
    "no-unused-vars": "off",
    "vue/return-in-computed-property": "off",
    "no-console": "off"
  }
}
