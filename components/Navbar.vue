<template>
  <Container>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-end">
          <NuxtLink to="menu" class="navbar-item">
            Menu
          </NuxtLink>
          <NuxtLink to="events" class="navbar-item">
            Events
          </NuxtLink>
          <NuxtLink to="contact" class="navbar-item">
            Contact
          </NuxtLink>
        </div>
      </div>
    </nav>
  </Container>
</template>

<style>
</style>
