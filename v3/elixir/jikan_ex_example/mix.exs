defmodule JikanExExample.MixProject do
  use Mix.Project

  def project do
    [
      app: :jikan_ex_example,
      version: "0.1.0",
      elixir: "~> 1.11",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:jikan_ex, ">=0.1.5"}
    ]
  end
end
