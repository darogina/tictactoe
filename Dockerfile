FROM fedora:30

LABEL name="tictactoe" \
      description="Tic-Tac-Toe where you can never win." \
      maintainer="David Rogina <nope@nope.com>"

WORKDIR /app

# Set up user permissions
RUN groupadd -g 61000 gamemaster && \
    useradd -g 61000 -l --no-create-home -s /bin/false -u 61000 gamemaster && \
    chmod g+s /app

COPY ./tictactoe.py /app/

RUN chown -R gamemaster:gamemaster /app && \
    chmod 750 /app/tictactoe.py

USER gamemaster

ENTRYPOINT ["python3", "/app/tictactoe.py"]

