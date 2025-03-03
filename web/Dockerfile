# Stage 1: Build
FROM oven/bun:latest AS build
WORKDIR /app
COPY package.json .
COPY bun.lock .
RUN bun install --frozen-lockfile
COPY . .
RUN bun run build

# Stage 2: Run
FROM oven/bun:latest
WORKDIR /app
COPY --from=build /app/build ./build
COPY --from=build /app/package.json .
