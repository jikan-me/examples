defmodule JikanExExample do
  @moduledoc """
  Examples for using JikanEx, taken from the docs
  https://hexdocs.pm/jikan_ex/JikanEx.Request.html
  """

  alias JikanEx.Request


  defp wait(), do: :timer.sleep(3000)

  def main do
    client = JikanEx.client()

    response = Request.anime!(client, 26165)
    IO.puts("Requested: " <> response["http_url"])
    IO.puts(response["title"])

    wait()

    response = Request.user!(client, "xinil", [:animelist, :all, 2], %{year: 2019})
    IO.puts("Requested: " <> response["http_url"])
    IO.puts("Number of entries: #{response["anime"] |> length()}")

  end
end
