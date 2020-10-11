<template>
  <section class="hero is-success is-fullheight background">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h1 class="title">
          <img src="/logo.png" alt="ACID">
        </h1>
        <h2 class="subtitle">
          Welcome back. Again.
        </h2>

        <div id="navigation">
          <div class="navbar">
            <div class="navbar-item">
              <NuxtLink to="/menu">Menu</NuxtLink>
            </div>
            <div class="navbar-item">
              <NuxtLink to="/events">Events</NuxtLink>
            </div>
            <div class="navbar-item">
              <NuxtLink to="/contact">Contact</NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
    <AnimatedCorner fuzz="100" position="topleft" />
    <AnimatedCorner position="bottomright" />
  </section>
</template>

<style scoped>
.background { 
  background: #6900ff !important;
  color: #ffffff;
  position: relative;
  overflow: hidden;
}

.navbar {
  justify-content: center;
}

.navbar a {
  color: rgba(255, 255, 255, 0.8);
  transition: color ease-in-out .2s;
}

.navbar a:hover {
  color: rgba(255, 255, 255, 1);
}
</style>

<script>
import Vue from 'vue'

export default Vue.extend({
  layout: 'empty',
})
</script>
