<?php
declare(strict_types=1);
require_once __DIR__ . '/bootstrap.php';
?><!doctype html>
<html lang="en"><head>
<?php echo canvas_head('Canvas | DrMarchand’s Laboratory'); ?>
<meta name="description" content="Canvas is the shared webpage foundation developed within DrMarchand’s Laboratory.">
</head><body>
<a class="canvas-skip" href="#main">Skip to content</a>
<header class="canvas-container"><p><strong>Canvas</strong> · DrMarchand’s Laboratory</p></header>
<main id="main" class="canvas-container">
<h1>Every great website begins with a Canvas.</h1>
<p>A shared foundation for organizing and presenting webpages, with reusable structure and independent site identities.</p>
<div class="canvas-grid">
<section class="canvas-card"><h2>Structure</h2><p>Predictable page foundations.</p></section>
<section class="canvas-card"><h2>Design</h2><p>Consistent styling without sacrificing identity.</p></section>
<section class="canvas-card"><h2>Components</h2><p>Reusable building blocks.</p></section>
</div>
</main><footer class="canvas-container"><p>Design Orchard LLC · Canvas v<?php echo htmlspecialchars(CANVAS_VERSION, ENT_QUOTES, 'UTF-8'); ?></p></footer>
</body></html>