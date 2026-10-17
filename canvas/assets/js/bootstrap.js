/* Canvas browser bootstrap v0.1.0: no remote execution or global overrides. */
(() => {
  'use strict';
  const version = '0.1.0';
  const ready = () => {
    document.documentElement.dataset.canvasVersion = version;
    document.dispatchEvent(new CustomEvent('canvas:ready', { detail: { version } }));
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready, { once: true });
  } else {
    ready();
  }
})();
