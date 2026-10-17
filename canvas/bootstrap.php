<?php
declare(strict_types=1);

/**
 * Canvas bootstrap v0.1.0.
 * Server-side initialization only. Do not expose private configuration.
 */
if (!defined('CANVAS_BOOTSTRAPPED')) {
    define('CANVAS_BOOTSTRAPPED', true);
    define('CANVAS_ROOT', __DIR__);
    define('CANVAS_VERSION', '0.1.0');

    function canvas_asset(string $path): string
    {
        $path = ltrim($path, '/');
        if ($path === '' || str_contains($path, '..') || !preg_match('~^[a-zA-Z0-9/_ .-]+$~', $path)) {
            throw new InvalidArgumentException('Invalid Canvas asset path');
        }
        return '/canvas/assets/' . implode('/', array_map('rawurlencode', explode('/', $path)));
    }

    function canvas_escape(string $value): string
    {
        return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    }

    function canvas_head(string $title, string $description = ''): string
    {
        $title = canvas_escape($title);
        $description = canvas_escape($description);
        $css = canvas_escape(canvas_asset('css/style.css'));
        $js = canvas_escape(canvas_asset('js/bootstrap.js'));
        return '<meta name="viewport" content="width=device-width, initial-scale=1">'
            . '<title>' . $title . '</title>'
            . '<meta name="description" content="' . $description . '">'
            . '<link rel="stylesheet" href="' . $css . '">'
            . '<script src="' . $js . '" defer></script>';
    }
}
