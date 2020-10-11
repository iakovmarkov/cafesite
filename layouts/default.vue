<template>
  <div class="layout">
    <div>
      <Navbar />
    </div>
    <div class="layout-content my-5 mx-3">
      <Nuxt />
    </div>
    <div class="layout-footer mt-5 pt-5">
      <Footer />
    </div>
  </div>
</template>

<style>
html {
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

html, body, #__nuxt, #__layout {
  height: 100%;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.layout-content {
  flex: 1 0 auto;
}

.layout-footer {
  flex-shrink: 0;
}
</style>
