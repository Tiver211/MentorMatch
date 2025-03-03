# Stage 1: Build
FROM oven/bun:latest AS build
WORKDIR /app
COPY package.json .
COPY bun.lock .
RUN bun install --production --frozen-lockfile
COPY . .
RUN bun run build

# Stage 2: Run
FROM oven/bun:latest
WORKDIR /app
COPY --from=build /app/build .
COPY --from=build /app/package.json .
COPY --from=build /app/node_modules ./node_modules
EXPOSE 3000
CMD ["bun", "run", "start"]
