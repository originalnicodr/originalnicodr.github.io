var allowedDomain = 'originalnicodr.github.io';
var gaID = 'G-DRR1CQZJM0';

// Check if the current hostname matches the allowed domain, to block forks from reporting to my analytics
if (window.location.hostname === allowedDomain) {
  var gaScript = document.createElement('script');
  gaScript.async = true;
  gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + gaID;
  document.head.appendChild(gaScript);

  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', gaID);
}
