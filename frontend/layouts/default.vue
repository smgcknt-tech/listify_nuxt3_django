<template>
  <div id="app">
    <header>
      <Header />
      <SideBar />
    </header>
    <main>
      <slot />
    </main>
  </div>
</template>

<style lang="scss">
#app {
  min-height: 100vh;
  display: grid;
  grid-template-rows: 3rem 1fr;
  grid-template-columns: 1fr;
  grid-template-areas:
    "header"
    "main";
  header {
    grid-area: header;
    @include background-color($primary);
    @include row;
    @include color;
  }
  main {
    grid-area: main;
    @include background-color;
    @include color($secondary);
  }
  > * {
    @include padding;
  }
}
</style>
