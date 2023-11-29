FROM library/caddy

COPY --from=local/reflex-app /app/.web/_static /srv


ADD Caddyfile /etc/caddy/Caddyfile

# Run caddy fmt to format the Caddyfile
RUN caddy fmt --overwrite