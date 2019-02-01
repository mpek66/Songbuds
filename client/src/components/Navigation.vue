<template>
  <b-navbar
    toggleable="sm"
    type="dark"
    variant="primary"
    sticky="true">
    <b-navbar-brand href="#">Songbuds</b-navbar-brand>
    <b-navbar-toggle
      target="navCollapse">
    </b-navbar-toggle>
    <b-collapse is-nav id="navCollapse">
      <b-navbar-nav class="ml-auto">
        <b-nav-item>Home</b-nav-item>
        <b-nav-item>Create</b-nav-item>
        <b-nav-item>Friends</b-nav-item>
        <b-nav-item>Account</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
