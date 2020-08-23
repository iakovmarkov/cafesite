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
      </div>
    </div>
    <AnimatedCorner fuzz="100" position="topleft" />
    <AnimatedCorner position="bottomright" />
  </section>
</template>

<style>
.background { 
  background: #6900ff !important;
  color: #ffffff;
  position: relative;
  overflow: hidden;
}
</style>
