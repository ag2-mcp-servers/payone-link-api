# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T08:19:25+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Path, Query
from pydantic import constr

from models import LinkCreateRequest, LinkResponse, PageLinkResponse

app = MCPProxy(
    contact={'email': 'info@payone.com', 'url': 'https://www.payone.com/kontakt/'},
    title='PAYONE Link API',
    version='v1',
    servers=[
        {
            'description': 'PAYONE Link API server url',
            'url': 'https://onelink.pay1.de/api',
        }
    ],
)


@app.get(
    '/v1/payment-links',
    tags=['payment_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_payment_links(
    page: Optional[int] = 0,
    limit: Optional[int] = 25,
    merchant_id: constr(pattern=r'[0-9]+') = Query(..., alias='merchantId'),
    account_id: constr(pattern=r'[0-9]+') = Query(..., alias='accountId'),
    portal_id: constr(pattern=r'[0-9]+') = Query(..., alias='portalId'),
    mode: constr(pattern=r'live|test') = ...,
):
    """
    List all payment links.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/payment-links',
    tags=['payment_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def create_payment_link(body: LinkCreateRequest = None):
    """
    Create a payment link.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/payment-links/{linkId}',
    tags=['payment_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_payment_link(
    link_id: constr(pattern=r'[0N1RWU4X6F8Z9ALBQC3EG5HJKM2PS7TVDY]{32}') = Path(
        ..., alias='linkId'
    )
):
    """
    Get payment link by id.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/v1/payment-links/{linkId}',
    tags=['payment_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def update_payment_link(
    link_id: constr(pattern=r'[0N1RWU4X6F8Z9ALBQC3EG5HJKM2PS7TVDY]{32}') = Path(
        ..., alias='linkId'
    ),
    body: LinkCreateRequest = None,
):
    """
    Update a payment link.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
