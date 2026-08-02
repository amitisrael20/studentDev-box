FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    gdb \
    valgrind \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
CMD ["bash"]