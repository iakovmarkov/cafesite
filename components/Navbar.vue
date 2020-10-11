<template>
  <Container>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <NuxtLink class="navbar-item" to="/">
          <Logo />
        </NuxtLink>
        <a
          role="button"
          :class="{ 'navbar-burger': true, 'burger': true, 'is-active': isMenuOpen }"
          aria-label="menu"
          :aria-expanded="isMenuOpen"
          data-target="navigation"
          @click="toggle"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navigation" :class="{ 'navbar-menu': true, 'is-active': isMenuOpen }">
        <div class="navbar-end">
          <div class="navbar-item" @click="toggle">
            <NuxtLink to="/menu">Menu</NuxtLink>
          </div>
          <div class="navbar-item" @click="toggle">
            <NuxtLink to="/events">Events</NuxtLink>
          </div>
          <div class="navbar-item" @click="toggle">
            <NuxtLink to="/contact">Contact</NuxtLink>
          </div>
        </div>
      </div>
    </nav>
  </Container>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  computed: {
    isMenuOpen() {
      return this.$store.state.menu.open
    },
  },
  methods: {
    ...mapMutations({
      toggle: 'menu/toggle',
    }),
  },
}
</script>

<style>
</style>
