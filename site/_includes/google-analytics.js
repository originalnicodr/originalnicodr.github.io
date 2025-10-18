var allowedDomain = 'originalnicodr.github.io';

// Check if the current hostname matches the allowed domain, to block forks from reporting to my analytics
if (window.location.hostname === allowedDomain) {
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3L3KV1JBV4');
}
